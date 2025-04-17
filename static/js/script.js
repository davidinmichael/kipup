window.addEventListener("DOMContentLoaded", () => {
	let colorModeToggle = document.getElementById("colorMode");
	colorModeToggle.addEventListener("click", () => {
		document.body.classList.toggle("dark-mode");
	});
	
	const menuToggle = document.getElementById("menuToggle");
	menuToggle.addEventListener("click", () => {
		console.log("Button Clicked");
		const navLinks = document.getElementById("navLinks");
		navLinks.classList.toggle("toggle-nav");
	});
});