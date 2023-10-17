import React, { useState, useEffect } from 'react';

function Shoes() {
	const [shoes, setShoes] = useState('');

	useEffect(() => {
		async function fetchData() {
			const response = await fetch('http://localhost:8080/api/shoes');

			if (response.ok) {
				const data = await response.json();

				console.log(data.shoes);

				setShoes(data.shoes);
			}
		}

		fetchData();
	}, []);

	return (
		<div>
			<h1>Shoes</h1>
			<table className="table table-striped">
				<thead>
					<tr>
						<th>Brand</th>
						<th>Model</th>
						<th>Color</th>
						<th>Bin</th>
						<th>Image</th>
					</tr>
				</thead>

				<tbody>
					{shoes &&
						shoes.map((shoe) => {
							return (
								<tr>
									<td>{shoe.manufacturer_name}</td>
									<td>{shoe.model_name}</td>
									<td>{shoe.color}</td>
									<td>{shoe.assigned_bin.closet_name}</td>
									<td>{shoe.picture_url}</td>
								</tr>
							);
						})}
				</tbody>
			</table>
		</div>
	);
}

export default Shoes;
