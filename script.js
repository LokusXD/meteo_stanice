const fetch_data = async () => {
	const req = await fetch("/api/data");
	const data = await req.json();
	
	document.querySelector("#temperature").innerText = data.temperature;
	document.querySelector("#humidity").innerText = data.humidity;
}

window.addEventListener("load", () => {
	fetch_data();
	setInterval(fetch_data, 5000);
});
