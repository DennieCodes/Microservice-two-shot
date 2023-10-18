import React, { useState, useEffect } from 'react';

function ShoesForm() {
	const [bins, setBins] = useState('');
	const [brand, setBrand] = useState('');
	const [model, setModel] = useState('');
	const [color, setColor] = useState('');
	const [image, setImage] = useState('');
	const [bin, setBin] = useState('');

	const handleBrandChange = (e) => setBrand(e.target.value);
	const handleModelChange = (e) => setModel(e.target.value);
	const handleColorChange = (e) => setColor(e.target.value);
	const handleImageChange = (e) => setImage(e.target.value);
	const handleBinChange = (e) => setBin(e.target.value);

	const handleSubmit = async (event) => {
		event.preventDefault();
		const data = {};
		data.manufacturer_name = brand;
		data.model_name = model;
		data.color = color;
		data.picture_url = image;
		data.assigned_bin = bin;

		const shoeUrl = 'http://localhost:8080/api/shoes/';
		const fetchConfig = {
			method: 'post',
			body: JSON.stringify(data),
			headers: {
				'Content-Type': 'application/json',
			},
		};

		const response = await fetch(shoeUrl, fetchConfig);

		if (response.ok) {
			const newShoe = await response.json();
			console.log(newShoe);

			setBrand('');
			setModel('');
			setColor('');
			setImage('');
			setBin('');
		}
	};

	const fetchData = async () => {
		const url = 'http://localhost:8100/api/bins/';

		try {
			const response = await fetch(url);

			if (response.ok) {
				const data = await response.json();

				setBins(data.bins);
			}
		} catch (error) {
			console.error(error);
		}
	};

	useEffect(() => {
		fetchData();
	}, []);

	return (
		<div className="shadow p-4 mt-4">
			<h3>Add a new shoe</h3>
			<form id="create-shoe-form" onSubmit={handleSubmit}>
				<div className="form-floating mb-2">
					<input
						onChange={handleBrandChange}
						value={brand}
						className="form-control"
						placeholder="Brand"
						required
						type="text"
						brand="brand"
						id="brand"
					/>
					<label htmlFor="brand">Brand</label>
				</div>

				<div className="form-floating mb-2">
					<input
						onChange={handleModelChange}
						value={model}
						className="form-control"
						placeholder="model"
						required
						type="text"
						name="model"
						id="model"
					/>
					<label htmlFor="model">Model</label>
				</div>

				<div className="form-floating mb-2">
					<input
						onChange={handleColorChange}
						value={color}
						className="form-control"
						placeholder="color"
						required
						type="text"
						name="color"
						id="color"
					/>
					<label htmlFor="color">color</label>
				</div>

				<div className="form-floating mb-2">
					<input
						onChange={handleImageChange}
						value={image}
						className="form-control"
						placeholder="image"
						required
						type="text"
						name="image"
						id="image"
					/>
					<label htmlFor="image">image</label>
				</div>

				<div className="mb-3">
					<select
						value={bin}
						required
						id="bin"
						name="bin"
						className="form-select"
						onChange={handleBinChange}
					>
						<option value="">Choose a bin</option>
						{bins &&
							bins.map((bin) => {
								return (
									<option key={bin.href} value={bin.href}>
										{bin.closet_name}
									</option>
								);
							})}
					</select>
				</div>
				<button className="btn btn-primary">Add Shoe</button>
			</form>
		</div>
	);
}

export default ShoesForm;
