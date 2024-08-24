var gets = document.querySelectorAll("*[get]")
console.log(gets)
gets.forEach((current) => {
    current.addEventListener("click", async (e) => {
        var request_url = current.getAttribute("get")
        // console.log(request_url)

        server_responce = await fetch(request_url).then(r => r.text())
        // console.log(server_responce)
        if (server_responce === "404") {
            // console.log(`error with ${request_url}: 404`)
            return -1
        }
        current.outerHTML = server_responce
    })
})

document.querySelector(".posts").addEventListener("change", (e) => {

    console.log("changed")
    var is_clickable = document.querySelectorAll("*[onclick]")
    is_clickable.forEach((c) => {
        c.addEventListener("click", e => {
            console.log("clicked")
        })
    })
})