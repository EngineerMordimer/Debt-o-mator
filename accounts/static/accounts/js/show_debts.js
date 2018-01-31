function toggleDebtsVisibility() {
    var func = document.getElementById("toggleDisplayDebts").innerHTML;

    if (func.indexOf("Hide") !== -1) {
        var elements = document.getElementsByClassName("paidDebts")

        for (var i = 0; i < elements.length; i++) {
            elements[i].style.display = "none";
        }
        document.getElementById("toggleDisplayDebts").innerHTML = "Show inactive debts";
        document.getElementById("debtsHeadline").innerHTML = "Active debts list:";
    }
    else {
        var elements = document.getElementsByClassName("paidDebts")

        for (var i = 0; i < elements.length; i++) {
            elements[i].style.display = null;
        }
        document.getElementById("toggleDisplayDebts").innerHTML = "Hide inactive debts";
        document.getElementById("debtsHeadline").innerHTML = "All debts list:";
    }
}
