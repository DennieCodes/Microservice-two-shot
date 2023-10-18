import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

function HatsList() {
    const [hats, setHats] = useState([]);

    const fetchData = async () => {
        const url = 'http://localhost:8090/api/hats/';
        const response = await fetch(url);
        
        if (response.ok) {
            const data = await response.json();
            setHats(data.hats);
            }
    }
    useEffect(() => {
        getHats();
    }, []);

    function getHats() {
        fetchData();
    }

    const deleteHat = async (e) => {
		const deleteHatUrl = `http://localhost:8090/api/hats/${e.target.value}`;

		const fetchConfig = {
			method: 'delete',
		};

		const response = await fetch(deleteHatUrl, fetchConfig);

		if (response.ok) {
			fetchData();
		}
	};


    return (
        <div className='row'>
        <div className='col-md-12'>
        <h1>Hats List</h1>
        <div>
            <Link to='/hats/new' className='btn btn-primary'>Add Hats</Link>
        </div>
        <table className="table table-striped">
            <thead>
                <tr>
                    <th>Hat Style</th>
                    <th>Color</th>
                    <th>Fabric Type</th>
                </tr>
            </thead>
            <tbody>
                {hats.map(hat => {
                    return (
                        <tr key={hat.id}>
                            <td>{hat.style_name}</td>
                            <td>{hat.color}</td>
                            <td>{hat.fabric}</td>
                            <td>{hat.location}</td>
                            <td><img src={hat.picture_url} alt="" height="100" /></td>
                            <td><button onClick={deleteHat} type="button" value={hat.id} className="btn btn-danger">Delete</button></td>
                        </tr>
                    );
                })}
            </tbody>
        </table>
        </div>
        </div>
    );
}





export default HatsList