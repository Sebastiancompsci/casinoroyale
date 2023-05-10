# API routes for user profile page.

from flask import jsonify, request, session
from flask import current_app as app


def get_tracked_teams():
    # Get user from session
    user = session.get('user', None)

    # If user is not logged in, return error
    if not user:
        return jsonify({'error': 'User not logged in.'}), 401

    # Get user's tracked teams
    cursor = app.config["conn"].cursor()

    # Fetch user by username.
    cursor.execute("SELECT * FROM users WHERE username = ?", (user,))
    user = cursor.fetchone()

    if not user:
        return jsonify({'error': 'Bad user.'}), 401

    # This is the command used to create the table in the database
    # CREATE TABLE tracked_teams (id INTEGER PRIMARY KEY, team_id INTEGER, user_id INTEGER)
    cursor.execute("SELECT * FROM tracked_teams WHERE user_id = ?", (user[0],))
    teams = cursor.fetchall()

    # We will fetch the team IDs from the tracked_teams table, then use those IDs to fetch the team names from the teams table
    team_ids = [team[1] for team in teams]

    # This is the command used to create the table in the database
    # CREATE TABLE teams (id INTEGER PRIMARY KEY, name TEXT)
    cursor.execute("SELECT * FROM teams WHERE id IN ({})".format(','.join('?' for _ in team_ids)), team_ids)
    teams = cursor.fetchall()

    teams = [{'id': team[0], 'name': team[1], 'imgUrl': team[2]} for team in teams]

    # Return teams
    return jsonify({'teams': teams}), 200


def get_teams():
    # Get teams
    cursor = app.config["conn"].cursor()

    # This is the command used to create the table in the database
    # CREATE TABLE teams (id INTEGER PRIMARY KEY, name TEXT)
    cursor.execute("SELECT * FROM teams")
    teams = cursor.fetchall()

    # Format to include names and images
    teams = [{'id': team[0], 'name': team[1], 'imgUrl': team[2]} for team in teams]

    # Return teams
    return jsonify({'teams': teams}), 200


def set_tracked_teams():
    # Get user from session
    user = session.get('user', None)

    # If user is not logged in, return error
    if not user:
        return jsonify({'error': 'User not logged in.'}), 401

    # Get teams from request
    teams = request.json.get('teams', None)

    # If teams is not in request, return error
    if not teams:
        return jsonify({'error': 'No teams provided.'}), 400

    print(teams)

    # Get user's tracked teams
    cursor = app.config["conn"].cursor()

    # Fetch user by username.
    cursor.execute("SELECT * FROM users WHERE username = ?", (user,))
    user = cursor.fetchone()

    if not user:
        return jsonify({'error': 'Bad user.'}), 401

    # This is the command used to create the table in the database
    # CREATE TABLE tracked_teams (id INTEGER PRIMARY KEY, team_id INTEGER, user_id INTEGER)
    cursor.execute("DELETE FROM tracked_teams WHERE user_id = ?", (user[0],))

    # Insert new tracked teams
    cursor.executemany("INSERT INTO tracked_teams (team_id, user_id) VALUES (?, ?)", [(team, user[0]) for team in teams])

    # Commit changes
    app.config["conn"].commit()

    # Return success
    return jsonify({'success': True}), 200