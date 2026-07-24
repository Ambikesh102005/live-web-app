document.getElementById('checkBtn').addEventListener('click', async () => {
    const statusText = document.getElementById('serverStatus');
    statusText.innerText = "कनेक्ट हो रहा है...";
    
    try {
        const res = await fetch('/api/status');
        const data = await res.json();
        statusText.innerText = data.status;
        statusText.style.color = "#3fb950";
    } catch (err) {
        statusText.innerText = "Offline 🔴";
        statusText.style.color = "#f85149";
    }
});
