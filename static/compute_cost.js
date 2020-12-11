function compute_cost(products, quantity) {
    let total = 0
    for (let product in products) {
        total += parseFloat((products[product] * quantity[product]).toFixed(2));

        document.getElementById("price" + product).innerText = (products[product] * quantity[product]).toFixed(2);
    }
    if (!no_products) {
        document.getElementById("total").innerText = "total price is: Rs" + total + "/-";
    }
};