let image_input = document.getElementById("id_image")
let table_input = document.getElementById("id_table")
let title_input = document.getElementById("id_title")
let description_input = document.getElementById("id_description")
let price_input = document.getElementById("id_price")
let special_input = document.getElementById("id_special_model")
let submit_button = document.getElementById("submit_button")
submit_button.addEventListener("click", function () {
    form_submit()
})

function setup() {
    let div = document.createElement("div");
    let node = document.createTextNode("title should not be empty");
    div.classList.add("invalid-feedback")
    div.id = "title_error"
    div.appendChild(node);
    title_input.parentElement.appendChild(div)
    div = document.createElement("div");
    node = document.createTextNode("image should not be empty");
    div.classList.add("invalid-feedback")
    div.id = "image_error"
    div.appendChild(node);
    image_input.parentElement.appendChild(div)
    div = document.createElement("div");
    node = document.createTextNode("description should not be empty");
    div.classList.add("invalid-feedback")
    div.id = "description_error"
    div.appendChild(node);
    description_input.parentElement.appendChild(div)
    div = document.createElement("div");
    node = document.createTextNode("price should not be empty/0");
    div.classList.add("invalid-feedback")
    div.id = "price_error"
    div.appendChild(node);
    price_input.parentElement.appendChild(div)
}

title_input.addEventListener("keyup", function () {
    is_title_valid = validate_title()
})
description_input.addEventListener("keyup", function () {
    is_description_valid = validate_description()
})
image_input.addEventListener("keyup", function () {
    is_image_valid = validate_image()
})
price_input.addEventListener("change", function () {
    is_price_valid = validate_price()
})
price_input.addEventListener("keyup", function () {
    is_price_valid = validate_price()
})

function form_submit() {
    if (!form_validate()) {
        alert("form is invalid check again")
        return
    }
    let image_text = image_input.value
    if (image_text === "" || image_text === "null") {
    } else {
        let images = image_text.split(/[\n ,]/)
        image_text = "{"
        let j = 0
        for (let i = 0; i < images.length; i++) {
            if (images[i] == "" || images[i] == " ") {
                j += 1
                continue
            }

            image_text += '"image' + (i + 1 - j) + '":"' + images[i] + '",'
        }
        image_text = image_text.slice(0, image_text.length - 1) + "}"
        image_input.value = image_text
    }
    let table_text = table_input.value;


    if (table_text === "" || table_text === "null") {
        table_input.value = "{}"

    } else {
        let table_items = table_text.split(/[\n ,]/);
        table_text = "{"
        console.log(table_items)
        j = 0
        for (let i = 0; i < table_items.length; i++) {
            if (table_items[i] == "" || table_items[i] == " ") {
                j += 1
                continue
            }
            let value = table_items[i].split(":");
            console.log(value)
            table_text += '"' + value[0] + '":"' + value[1] + '",';
        }
        table_text = table_text.slice(0, table_text.length - 1) + "}"
        table_input.value = table_text
    }

    document.getElementById("form").submit()
}

function form_validate() {
    validate_image()
    validate_description()
    validate_price()
    validate_title()
    if (is_price_valid && is_title_valid && is_description_valid && is_image_valid) {
        return true
    }
    return false
}

function validate_title() {
    if (title_input.value == "") {
        document.getElementById("title_error").innerText = "title should not be empty"
        title_input.classList.add("is-invalid")
        return false
    }
    if (title_input.value.length > 150) {
        document.getElementById("title_error").innerText = "title should be less than 150 characters"
        title_input.classList.add("is-invalid")
        return false
    }
    title_input.classList.remove("is-invalid")
    return true
}

function validate_price() {
    if (price_input.value == "") {
        document.getElementById("price_error").innerText = "price should not be empty"
        price_input.classList.add("is-invalid")
        return false
    }
    if (price_input.value <= 0) {
        document.getElementById("price_error").innerText = "price should be positive "
        price_input.classList.add("is-invalid")
        return false
    }
    price_input.classList.remove("is-invalid")
    return true
}

function validate_description() {
    if (description_input.value == "") {
        document.getElementById("description_error").innerText = "description should not be empty"
        description_input.classList.add("is-invalid")
        return false
    }
    if (description_input.value.length > 1000) {
        document.getElementById("description_error").innerText = "description should be less than 1000 characters"
        description_input.classList.add("is-invalid")
        return false
    }
    description_input.classList.remove("is-invalid")
    return true
}

function validate_image() {
    if (image_input.value == "" || image_input.value == "null") {
        document.getElementById("image_error").innerText = "image should not be empty"
        image_input.classList.add("is-invalid")
        return false
    }
    if (image_input.value.split(/[\n ,]/).length > 10) {
        document.getElementById("image_error").innerText = "no of images should be less than 10"
        image_input.classList.add("is-invalid")
        return false
    }
    image_input.classList.remove("is-invalid")
    return true
}
