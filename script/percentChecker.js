$(document).ready(function()
{



	var checked=0; 

	$('.checker').on('click', function()
	{
		var numOfCheckers = $('.checker').length; 
		if( $(this).is(':checked') )
		{
			checked+=1;
		}
		else
		{
			checked-=1; 
		}

		var propotionChecked = (checked/numOfCheckers) * 100; 

		$('.perc').html( propotionChecked + "% Checked"); 

		if(propotionChecked<=25)
		{
			$('.perc').css('background-color','red'); 
		}
		else if(propotionChecked>=25 && propotionChecked<=50)
		{
			$('.perc').css('background-color','yellow'); 
		}
		else if(propotionChecked>=75 && propotionChecked<=100)
		{
			$('.perc').css('background-color','green'); 
		}


		
	}); 
	


}); 