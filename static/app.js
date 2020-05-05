const name = document.querySelector("#name")
const email = document.querySelector("#email")
const message = document.querySelector("#message")
const popup = document.querySelector("#popup")
const clear = document.querySelector("#clear")

// removes popup
clear.addEventListener("click", () => {
   popup.style.display = "none"
})

document.addEventListener("submit", (e) => {
   const form = e.target

   fetch(form.action, {
      method: form.method,
      body: new FormData(form),
   }).then((data) => {
      popup.style.display = "flex"
      name.value = ""
      email.value = ""
      message.value = ""
   })

   e.preventDefault()
})
