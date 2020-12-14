function form_submit() {
            let image_text = document.getElementById("id_image").value
            let images = image_text.split(/["\n ,"]/)
            image_text = "{"

            for (let i = 0; i < images.length; i++) {
                image_text += '"image' + (i + 1) + '":"' + images[i] + '",'
            }
            image_text = image_text.slice(0, image_text.length - 1) + "}"
            document.getElementById("id_image").value = image_text
            document.getElementById("form").submit()
        }




