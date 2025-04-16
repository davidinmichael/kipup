window.addEventListener("DOMContentLoaded", () => {
	let colorModeToggle = document.getElementById("colorMode");
	console.log("Hello");
	colorModeToggle.addEventListener("click", () => {
		console.log("Button Clicked");
		
		let body = document.getElementById("body");
		document.body.classList.toggle("dark-mode");
	});
});