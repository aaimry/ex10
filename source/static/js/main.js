function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


async function accept(event) {
    let pk = event.currentTarget.dataset.pk
    let pathname = window.location.pathname
    let csrftokem = getCookie('csrftoken')
    let url = '/api/advertisement/accept/'.replace(pathname, '')
    console.log(url)
    let response = await fetch(url, {
        method: 'POST',
        body: JSON.stringify({'id': pk, 'status': 'published'}),
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftokem
        }
    })
    if (response.ok) {
    } else {
        alert('Что-то пошло не так...')
    }
}

async function reject(event) {
    let pk = event.currentTarget.dataset.pk
    let pathname = window.location.pathname
    let moderator_block = document.getElementById('moderator_block' + pk)
    let csrftokem = getCookie('csrftoken')
    let url = '/api/advertisement/reject/'.replace(pathname, '')
    let response = await fetch(url, {
        method: 'POST',
        body: JSON.stringify({'id': pk, 'status': 'rejected'}),
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftokem
        }
    })
    if (response.ok) {
        moderator_block.remove()
    } else {
        alert('Что-то пошло не так...')
    }
}