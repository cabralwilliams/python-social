const btnUp = document.querySelector('#upvote');
const btnDown = document.querySelector('#downvote');

async function upvote(event) {
    event.preventDefault();
    const userId = parseInt(document.querySelector("#user_id").value);
    const postId = parseInt(document.querySelector("#post_id").value);

    const response = await fetch('/api/posts/upvote', {
        method: "PUT",
        body: JSON.stringify({
            post_id: postId,
            user_id: userId
        }),
        headers: { "Content-Type": "application/json" }
    });

    if(response.ok) {
        window.location.replace(`/posts/${postId}`);
    } else {
        alert(response.statusText);
    }
}

async function downvote(event) {
    event.preventDefault();
    const userId = parseInt(document.querySelector("#user_id").value);
    const postId = parseInt(document.querySelector("#post_id").value);

    const response = await fetch('/api/posts/downvote', {
        method: "PUT",
        body: JSON.stringify({
            post_id: postId,
            user_id: userId
        }),
        headers: { "Content-Type": "application/json" }
    });

    if(response.ok) {
        window.location.replace(`/posts/${postId}`);
    } else {
        alert(response.statusText);
    }
}

btnUp.addEventListener('click', upvote);
btnDown.addEventListener('click', downvote);

async function postComment(event) {
    event.preventDefault();

    const userId = parseInt(document.querySelector("#user_id").value);
    const postId = parseInt(document.querySelector("#post_id").value);
    const commentText = document.querySelector("#comment_text").value.trim();

    if(commentText) {
        const response = await fetch(`/api/comments`, {
            method: "POST",
            body: JSON.stringify({
                user_id: userId,
                post_id: postId,
                comment_text: commentText
            }),
            headers: { "Content-Type": "application/json" }
        });

        if(response.ok) {
            window.location.replace(`/posts/${postId}`);
        } else {
            alert(response.statusText);
        }
    }
    
}

document.querySelector("#add-comment").addEventListener("submit", postComment);