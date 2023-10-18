import React, { useEffect, useState } from "react";

function HatForm() {
    //style name
    const [styleName, setStyleName] = useState("");
    //fabric
    const [fabric, setFabric] = useState("");
    //color
    const [color, setColor] = useState("");
    //url
    const [url, setUrl] = useState("");
    //location
    const [location, setLocation] = useState("");

    //get list of locations[]
    const [locations, setLocations] = useState([]);

    const handleNameChange = (e) => {
        const value = e.target.value;
        setStyleName(value);
    }
    const handleFabricChange = (e) => {
        const value = e.target.value;
        setFabric(value);
    }
    const handleColorChange = (e) => {
        const value = e.target.value;
        setColor(value);
    }
    const handleUrlChange = (e) => {
        const value = e.target.value;
        setUrl(value);
    }
    const handleLocationChange = (e) => {
        const value = e.target.value;
        setLocation(value);
    }

    const handleSubmit = async (e) => {
        e.preventDefault();
        const data = {};
        data.style_name = styleName; //<< The issue might just be this
        data.fabric = fabric;
        data.color = color;
        data.photo_url = url;
        data.location = location;

        const hatsUrl = `http://localhost:8090${location}hats/`;
        const fetchConfig = {
            method: "POST",
            body: JSON.stringify(data),
            headers: {
                "Content-Type": "application/json"
            }
        };
        const response = await fetch(hatsUrl, fetchConfig);
        if (response.ok) {

            const newHat = await response.json();
            console.log(newHat);
            setStyleName("");
            setFabric("");
            setColor("");
            setUrl("");
            setLocation("");
            //window.location.reload();
        }

  
  
  
      }
      const fetchData = async () => {
        const url = `http://localhost:8100/api/locations/`;
        const response = await fetch(url);
        if (response.ok) {
            const data = await response.json();
            console.log("fetch response: ", data);
            setLocations(data.locations);
        }
    }
      useEffect(() => {
        fetchData();
    }, []);  


    return (
        <div className="my-5 container">
      <div className="row">
        <div className="col col-sm-auto">
          <img width="300" className="bg-white rounded shadow d-block mx-auto mb-4" alt="logo" src="/logo.svg" />
        </div>
        <div className="col">
          <div className="card shadow">
            <div className="card-body">
              <form onSubmit={handleSubmit} id="hat-form">
                <h1 className="card-title">Add a new Hat</h1>
                <p className="mb-3">
                  Please create a new hat.
                </p>
                  <div className="col">
                      <div className="form-floating mb-3">
                        <input onChange={handleNameChange} required placeholder="Style name" type="text" id="style_name" name="style_name" className="form-control" value={styleName}/>
                        <label htmlFor="style_name">Style Name</label>
                      </div>
                  </div>
                  <div className="col">
                    <div className="form-floating mb-3">
                        <input onChange={handleFabricChange} required placeholder="Fabric" type="text" id="fabric" name="fabric" className="form-control" value={fabric}/>
                        <label htmlFor="fabric">Fabric</label>
                    </div>
                  </div>
                  <div className="col">
                    <div className="form-floating mb-3">
                        <input onChange={handleColorChange} required placeholder="Color" type="text" id="color" name="color" className="form-control" value={color}/>
                        <label htmlFor="color">Color</label>
                    </div>
                  </div>
                  <div className="col">
                    <div className="form-floating mb-3">
                        <input onChange={handleUrlChange} required placeholder="URL" type="url" id="url" name="url" className="form-control" value={url}/>
                        <label htmlFor="url">Hat Picture URL</label>
                    </div>
                  </div>
                  <div className="form-floating mb-3">
                    <select onChange={handleLocationChange} name="location" id="location"  value={location}>
                      <option key="default" value="">Choose A Closet</option>
                      {locations.map(location => {
                        return (
                          <option key={location.href} value={location.href}>{location.closet_name}</option>
                        )
                      })}
                    </select>
                  </div>

                  <div className="col">
                    <button type="submit"  onClick={() => handleSubmit()}  className="btn btn-primary">Submit</button>
                  </div>
              </form>
              </div>
              </div>
              </div>
              </div>
              </div>

            )
}

export default HatForm;
