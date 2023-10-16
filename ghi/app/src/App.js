import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './MainPage';
import Nav from './Nav';
import Shoes from './Shoes';

function App() {
	return (
		<BrowserRouter>
			<Nav />
			<div className="container">
				<Routes>
					<Route path="/" element={<MainPage />} />
					<Route path="/shoes" element={<Shoes />} />
				</Routes>
			</div>
		</BrowserRouter>
	);
}

export default App;
