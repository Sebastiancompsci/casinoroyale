To run the TailwindCSS compiler, please run the following command:

```bash
npx tailwindcss -i ./static/css/main.css -o ./static/css/dist.css --watch --minify
```

This is also included in the package.json file as a script, so you can run it with:

```bash
npm run tailwind
```

Note: you need to have Node and NPM installed on your machine for this to work.
If you prefer not to use these tools or are confused please ask me to compile for you.

[Docs](https://tailwindcss.com/)