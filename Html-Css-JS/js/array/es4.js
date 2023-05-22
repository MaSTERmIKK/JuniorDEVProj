// Ricerca di un elemento nell'array
var fruits = ["Mela", "Banana", "Arancia", "Kiwi"];
var searchItem = "Banana";
var index = fruits.indexOf(searchItem);
if (index !== -1) {
	console.log(searchItem + " trovato all'indice " + index);
} else {
	console.log(searchItem + " non trovato nell'array.");
}
