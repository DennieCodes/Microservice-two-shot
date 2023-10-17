import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import ShoesForm from './ShoesForm';

function Shoes() {
	const [shoes, setShoes] = useState('');
	const [shoeForm, setShoeForm] = useState(false);

	const handleDeleteShoe = async (e) => {
		const deleteShoeUrl = `http://localhost:8080/api/shoes/${e.target.value}`;

		const fetchConfig = {
			method: 'delete',
		};

		const response = await fetch(deleteShoeUrl, fetchConfig);

		if (response.ok) {
			console.log('Shoe was deleted');
		}
	};

	const useToggle = () => {
		setShoeForm(!shoeForm);
	};

	useEffect(() => {
		async function fetchData() {
			const response = await fetch('http://localhost:8080/api/shoes');

			if (response.ok) {
				const data = await response.json();

				setShoes(data.shoes);
			}
		}

		fetchData();
	}, []);

	return (
		<div>
			<h1>Shoes</h1>

			<button className="btn btn-primary mt-2 mb-2" onClick={useToggle}>
				Add a Shoe
			</button>

			{shoeForm ? (
				<div>
					<ShoesForm />
				</div>
			) : (
				<table className="table table-striped">
					<thead>
						<tr>
							<th>Brand</th>
							<th>Model</th>
							<th>Color</th>
							<th>Bin</th>
							<th>Image</th>
							<th></th>
						</tr>
					</thead>

					<tbody>
						{shoes &&
							shoes.map((shoe) => {
								// console.log(shoe.id);
								return (
									<tr>
										<td>{shoe.manufacturer_name}</td>
										<td>{shoe.model_name}</td>
										<td>{shoe.color}</td>
										<td>{shoe.assigned_bin.closet_name}</td>
										<td>{shoe.picture_url}</td>
										<td>
											<button
												value={shoe.id}
												className="btn btn-danger"
												onClick={handleDeleteShoe}
											>
												Delete
											</button>
										</td>
									</tr>
								);
							})}
					</tbody>
				</table>
			)}
		</div>
	);
}

export default Shoes;
