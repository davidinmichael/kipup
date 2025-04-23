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

	let submitBtn = document.getElementById("regSubmitBtn");
	let passwordError = document.getElementById("passwordError");
	let emailError = document.getElementById("emailError");
	let agree = document.getElementById("agree");

	agree.addEventListener("click", () => {
		if (!agree.checked) {
			submitBtn.disabled = true;
		} else {
			emailError.textContent = "";
		}
	});

	
	let regForm = document.getElementById("registerForm");
	regForm.addEventListener("submit", async (e) => {
		e.preventDefault();
		let email = e.target.email.value;
		let password = e.target.password.value;
		let confirmPassword = e.target.confirm_password.value;
		
		let formValues = {
			first_name: e.target.first_name.value,
			last_name: e.target.last_name.value,
			email: e.target.email.value,
			gender: e.target.gender.value,
			password: e.target.password.value
		}
		
		if (email === "") {
			setTimeout(() => {
				emailError.textContent = "Error in email";
			}, 1000);
		} else if (email.includes("admin")) {
			emailError.textContent = "Email cannot contain admin keyword";

		} else if (password !== confirmPassword) {
			passwordError.textContent = "Passwords do not match."
		} else {
			try {
				const response = await fetch("/account/api/register/", {
					method: "POST",
					headers: {
						"Content-Type": "application/json"
					},
					body: JSON.stringify(formValues)
				});
				console.log(response);
				if (response.ok) {
					alert("User created successfully, continue to login.");
					window.location.href = "/account/login/";
				}
			} catch {
				console.log("Error");
			}
		}

	});
});