for (let i = 1; i < 6; i++) {
    if ((rating - i) >= 0) {
        document.getElementById("ostar" + i).classList.add("fa-star")
        document.getElementById("ostar" + i).classList.add("fill_star")
        continue
    }
    if ((rating - i + 0.5) >= 0) {
        document.getElementById("ostar" + i).classList.add("fa-star-half-full")
        document.getElementById("ostar" + i).classList.add("fill_star")
        continue
    }
    document.getElementById("ostar" + i).classList.add("fa-star")
}


function check_stars() {
    let stars = document.getElementsByName("rate")
    for (let i = 0; i < 5; i++) {
        if (stars[i].checked) {
            for (let j = 1; j <= 5; j++) {
                if (j <= i) {
                    document.getElementById("lable" + j).classList.add("sudo_check")
                } else
                    document.getElementById("lable" + j).classList.remove("sudo_check")
            }
        }
    }
}

function submit_form() {
    let stars = document.getElementsByName("rate")
    for (let i = 0; i < 5; i++) {
        if (stars[i].checked) {
            document.getElementById("id_rating").value = i + 1
        }
    }
    document.getElementById("form").submit()
}

window.onload = function () {
    if (document.getElementById("id_rating") != null)
        document.getElementById("id_rating").parentElement.hidden = true;
    if (total_ratings == 0) {
        document.getElementById("rating_block").innerHTML = "<p>no reviews</p>"
    }
}