import Carousel from '../components/carousel.jsx';

$('.carousel').carousel({
  interval: 1000 * 4
});

var temp = document.createElement("div");
ReactDOM.render(
	<Carousel />,
	temp
);
var container = document.getElementById("space-carousel");
container.replaceChild(temp.querySelector("#react-carousel"), document.getElementById("react-carousel"));
