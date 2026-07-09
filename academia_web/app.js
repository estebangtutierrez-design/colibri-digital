function saludarBuho() {
  const msgs = [
    "🦉 ¡Bienvenido a Lucas EGA Academy! Cada capítulo te acerca a tu meta.",
    "🦉 Recuerda: la práctica hace al maestro. ¡Empieza tu primer curso!",
    "🦉 El conocimiento es poder. ¡Vamos a programar!",
    "🦉 Esteban confía en ti. ¡No lo defraudes!"
  ];
  alert(msgs[Math.floor(Math.random() * msgs.length)]);
}

function getToken() { return localStorage.getItem("token"); }
function getUser() {
  try { return JSON.parse(localStorage.getItem("usuario")); } catch(e) { return null; }
}

function apiPost(path, data) {
  const t = getToken();
  return fetch(path, {
    method: "POST",
    headers: {"Content-Type": "application/json", ...(t ? {"Authorization": "Bearer " + t} : {})},
    body: JSON.stringify(data)
  }).then(r => r.json());
}

function apiGet(path) {
  const t = getToken();
  return fetch(path, {headers: t ? {"Authorization": "Bearer " + t} : {}}).then(r => r.json());
}
