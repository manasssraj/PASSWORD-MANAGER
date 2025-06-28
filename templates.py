    <!DOCTYPE html>
<html>
<head>
    <title>Password Manager</title>
    <style>
        body { font-family: Arial; margin: 40px; }
        input, button { margin: 5px; padding: 8px; }
    </style>
</head>
<body>
    <h1>Password Manager</h1>
    <form action="/save" method="POST">
        <input type="text" name="website" placeholder="Website" required><br>
        <input type="text" name="username" placeholder="Username" required><br>
        <input type="password" name="password" placeholder="Password" required><br>
        <button type="submit">Save Password</button>
    </form>

    <br><br>
    <button onclick="fetchPasswords()">View Saved Passwords</button>
    <pre id="output"></pre>

    <script>
        function fetchPasswords() {
            fetch('/get')
                .then(res => res.json())
                .then(data => {
                    document.getElementById('output').textContent = JSON.stringify(data, null, 4);
                });
        }
    </script>
</body>
</html>
