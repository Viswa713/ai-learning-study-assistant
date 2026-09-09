const API_URL = "http://127.0.0.1:8000";

const chatMessages =
document.getElementById("chat-messages");

const messageInput =
document.getElementById("message-input");

const sendButton =
document.getElementById("send-button");

const statusDot =
document.getElementById("status-dot");

const statusText =
document.getElementById("status-text");

/* ADD MESSAGE */

function addMessage(role, content) {

const message =
    document.createElement("div");

message.className =
    `message ${role}`;


const label =
    document.createElement("div");

label.className =
    "message-label";

label.textContent =
    role === "user"
        ? "YOU"
        : "AI ASSISTANT";


const messageContent =
    document.createElement("div");

messageContent.className =
    "message-content";

messageContent.textContent =
    content;


message.appendChild(label);

message.appendChild(
    messageContent
);

chatMessages.appendChild(message);


chatMessages.scrollTop =
    chatMessages.scrollHeight;

}

/* LOADING MESSAGE */

function addLoadingMessage() {

const message =
    document.createElement("div");

message.className =
    "message assistant";

message.id =
    "loading-message";


const label =
    document.createElement("div");

label.className =
    "message-label";

label.textContent =
    "AI ASSISTANT";


const content =
    document.createElement("div");

content.className =
    "message-content";

content.textContent =
    "Analyzing your request...";


message.appendChild(label);

message.appendChild(content);

chatMessages.appendChild(message);


chatMessages.scrollTop =
    chatMessages.scrollHeight;

}

/* REMOVE LOADING */

function removeLoadingMessage() {

const loadingMessage =
    document.getElementById(
        "loading-message"
    );

if (loadingMessage) {
    loadingMessage.remove();
}

}

/* BACKEND STATUS */

async function checkBackend() {

try {

    const response =
        await fetch(
            `${API_URL}/health`
        );


    if (!response.ok) {
        throw new Error(
            "Backend unavailable"
        );
    }


    statusDot.style.background =
        "#22c55e";

    statusText.textContent =
        "Connected";


} catch (error) {

    statusDot.style.background =
        "#ef4444";

    statusText.textContent =
        "Backend offline";
}

}

/* SEND MESSAGE */

async function sendMessage(customMessage = null) {

const message =
    customMessage !== null
        ? customMessage.trim()
        : messageInput.value.trim();


if (!message) {
    return;
}


addMessage(
    "user",
    message
);


messageInput.value = "";

messageInput.disabled =
    true;

sendButton.disabled =
    true;


addLoadingMessage();


try {

    const response =
        await fetch(
            `${API_URL}/chat`,
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    message: message
                })
            }
        );


    const data =
        await response.json();


    if (!response.ok) {

        throw new Error(
            data.detail ||
            "Request failed."
        );
    }


    removeLoadingMessage();


    addMessage(
        "assistant",
        data.response
    );


} catch (error) {

    removeLoadingMessage();


    addMessage(
        "assistant",
        `Unable to connect to the AI assistant. ${error.message}`
    );


} finally {

    messageInput.disabled =
        false;

    sendButton.disabled =
        false;

    messageInput.focus();
}

}

/* SEND BUTTON */

sendButton.addEventListener(
"click",
function () {
sendMessage();
}
);

/* ENTER TO SEND */

messageInput.addEventListener(
"keydown",
function (event) {

    if (
        event.key === "Enter" &&
        !event.shiftKey
    ) {

        event.preventDefault();

        sendMessage();
    }
}

);

/* QUICK ACTIONS */

document
.querySelectorAll(
".quick-action"
)
.forEach(
function (button) {

        button.addEventListener(
            "click",
            function () {

                const prompt =
                    button.dataset.prompt;

                sendMessage(prompt);
            }
        );
    }
);

/* SIDEBAR TOOLS */

document
.querySelectorAll(
".tool-card"
)
.forEach(
function (button) {

        button.addEventListener(
            "click",
            function () {

                document
                    .querySelectorAll(
                        ".tool-card"
                    )
                    .forEach(
                        function (item) {
                            item.classList.remove(
                                "active"
                            );
                        }
                    );


                button.classList.add(
                    "active"
                );


                const prompt =
                    button.dataset.prompt;


                sendMessage(prompt);
            }
        );
    }
);

/* INITIAL BACKEND CHECK */

checkBackend();

/* PERIODIC STATUS CHECK */

setInterval(
checkBackend,
10000
);