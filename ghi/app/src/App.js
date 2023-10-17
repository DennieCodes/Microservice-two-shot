import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './MainPage';
import Nav from './Nav';
import Shoes from './Shoes';
import HatsForm from "./HatsForm"
import HatsList from './HatsList';


function App() {
	return (
		<BrowserRouter>
			<Nav />
			<div className="container">
				<Routes>
					<Route path="/" element={<MainPage />} />
					<Route path="/shoes" element={<Shoes />} />
          			<Route path="/hats" element={<HatsList />} />
					<Route path="hats">
           			 	<Route path="/hats/new" element={<HatsForm />} />
          			</Route>

				</Routes>
		
			</div>
		</BrowserRouter>
	);
}

export default App;
