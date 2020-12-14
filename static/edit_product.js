let is_title_valid = true
let is_price_valid = true
let is_description_valid = true
let is_image_valid = true
window.onload = function () {
    setup()
    let image_text = document.getElementById("id_image").value
    let images = JSON.parse(image_text);
    image_text = ""
    for (let image in images) {
        image_text += images[image] + "\n"
    }
    document.getElementById("id_image").value = image_text
    let table_text = document.getElementById("id_table").value
    let tables = JSON.parse(table_text);
    table_text = ""
    for (let table in tables) {
        table_text += `${table}:${tables[table]} \n`
    }
    document.getElementById("id_table").value = table_text
}