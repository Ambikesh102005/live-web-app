document.getElementById('contactForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const name = document.getElementById('senderName').value;
    const message = document.getElementById('senderMsg').value;
    const responseMsg = document.getElementById('responseMsg');

    responseMsg.style.color = "#58a6ff";
    responseMsg.innerText = "भेजा जा रहा है...";

    try {
        const res = await fetch('/api/contact', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, message })
        });

        const data = await res.json();

        if (data.success) {
            responseMsg.style.color = "#3fb950";
            responseMsg.innerText = data.message;
            document.getElementById('senderName').value = '';
            document.getElementById('senderMsg').value = '';
        } else {
            responseMsg.style.color = "#f85149";
            responseMsg.innerText = data.message;
        }
    } catch (err) {
        responseMsg.style.color = "#f85149";
        responseMsg.innerText = "सर्वर से कनेक्ट नहीं हो सका!";
    }
});
