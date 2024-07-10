/**
 * Function to close the toast message box.
 * Returns no values.
 */
const toast = () => {
    const toastElement = document.getElementById("message-box");
    const closeToastButton = toastElement.querySelector('[aria-label="delete"]');

    const closeToast = () => {
        // Remove the message element from the DOM
        toastElement.remove();
    }

    closeToastButton.addEventListener("click", () => {
        closeToast();
    });

}

document.addEventListener("DOMContentLoaded", toast);