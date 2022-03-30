$(document).ready(function()
{
    colors_array = []
	let color
		$('button').click(function()
			{
			color = [$(this).css("background-color")]

			//store rgb color values in colors_array
			colors_array.push(color)

            //change squares background-color randomly
            carres = $('.carre')
            $(carres[Math.floor(Math.random()*carres.length)]).css('background-color', color)

            /**pb 1 : the same squares get colored
            -> implementing a each loop over div doesn't work, as "color" variable seems to get emptied outside of the click event.
            pb 2 : display the same colors when the page is refreshed
            -> following, colors_array is also empty**/
        })

})