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
						<th>Name</th>
					</tr>
				</thead>

				<tbody>
					{shoes &&
						shoes.map((shoe) => {
							return (
								<tr>
									<td>{shoe.name}</td>
								</tr>
							);
						})}
				</tbody>
			</table>
		</div>
	);
}

export default Shoes;
