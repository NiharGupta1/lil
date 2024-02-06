---
layout: default
permalink: /login
title: Login
---
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ page.title }}</title>
</head>
<body>
<form action="javascript:login_user()">
    <p><label>
        User ID:
        <input type="text" name="uid" id="uid" required>
    </label></p>
    <p><label>
        Password:
        <input type="password" name="password" id="password" required>
    </label></p>
    <p>
        <button>Login</button>
    </p>
</form><script type="module">
    import { uri, options } from '{{ site.baseurl }}/assets/js/api/config.js';function login_user(){
         const url = uri + '/api/users/authenticate';const body = {
            uid: document.getElementById("uid").value,
            password: document.getElementById("password").value,
        };  const authOptions = {
            ...options,
            method: 'POST',
            cache: 'no-cache',
            body: JSON.stringify(body)};
        fetch(url, authOptions)  .then(response => {
            if (!response.ok) {
                const errorMsg = 'Login error: ' + response.status;
                console.log(errorMsg);
                return;
            }
            window.location.href = "{{ site.baseurl }}/";  })
        .catch(err => {
            console.error(err);
        }); }
    window.login_user = login_user;
</script>

<a href="{{ site.baseurl }}/signup">Signup</a>

</body>
</html>
