import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

function Hats() {
    const [hats, setHats] = useState([]);

    const fetchData = async () => {
        const url = 'http://localhost:8090/api/hats/';
        const response = await fetch(url);
        console.log(response);
        if (response.ok) {
            const data = await response.json();
            setHats(data.hats);
            console.log(data.hats);
        }
    }
    useEffect(() => {
        getHats();
    }, [fetchData]);

    function getHats() {
        fetchData();
    }

    function deleteHat(id) {
        fetch(`http://localhost:8090/api/hats/${id}`, {
            method: 'DELETE'
        }).then((result) => {
            result.json().then((resp) => {
                console.warn(resp)
                getHats();
            })
        })
    }

    
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
                            <td>{hat.style}</td>
                            <td>{hat.color}</td>
                            <td>{hat.fabric}</td>
                            <td>{hat.location}</td>
                            <td><img src={hat.picture_url} alt="" height="100" /></td>
                            <td><button onClick={() => deleteHat(hat.id)} type="button" className="btn btn-danger">Delete</button></td>
                        </tr>
                    );
                })}
            </tbody>
        </table>
        </div>
        </div>
    );
}





export default Hats