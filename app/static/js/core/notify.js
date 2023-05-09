function errorNotification(message) {
    new Noty({
        type: 'error',
        layout: 'topRight',
        theme: 'sunset',
        text: message,
        timeout: 3000,
        progressBar: true,
        closeWith: ['click', 'button'],
        animation: {
            open: 'noty_effects_open', close: 'noty_effects_close'
        }
    }).show();
}

function successNotification(message) {
    new Noty({
        type: 'success',
        layout: 'topRight',
        theme: 'sunset',
        text: message,
        timeout: 3000,
        progressBar: true,
        closeWith: ['click', 'button'],
        animation: {
            open: 'noty_effects_open', close: 'noty_effects_close'
        }
    }).show();
}

function warningNotification(message) {
    new Noty({
        type: 'warning',
        layout: 'topRight',
        theme: 'sunset',
        text: message,
        timeout: 3000,
        progressBar: true,
        closeWith: ['click', 'button'],
        animation: {
            open: 'noty_effects_open', close: 'noty_effects_close'
        }
    }).show();
}

function infoNotification(message) {
    new Noty({
        type: 'info',
        layout: 'topRight',
        theme: 'sunset',
        text: message,
        timeout: 3000,
        progressBar: true,
        closeWith: ['click', 'button'],
        animation: {
            open: 'noty_effects_open', close: 'noty_effects_close'
        }
    }).show();
}