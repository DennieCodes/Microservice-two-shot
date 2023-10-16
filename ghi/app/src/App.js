import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './MainPage';
import Nav from './Nav';
import Shoes from './Shoes';
import Hats from "./Hats"


function App() {
	return (
		<BrowserRouter>
			<Nav />
			<div className="container">
				<Routes>
					<Route path="/" element={<MainPage />} />
					<Route path="/shoes" element={<Shoes />} />
          <Route path="/hats" element={<Hats />} />
				</Routes>
			</div>
		</BrowserRouter>
	);
}

export default App;
