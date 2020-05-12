## A CLI for translating and generating audio files</br>
</br>
</br>
trscli \<format\> \<input language\>-\<output language\> \<file\></br>
## How to use it:</br>
	trscli uses a three options.</br>
	* A format</br>
	* A language option</br>
	* A file</br>
</br>
	The format option specifies the output format of the audio file. It uses the following format: \<translate (t) or don't translate (u)\>,\<slow factor\>,\<pause\>.</br>
	Format "t,1,2" will produce an audio file with each of the lines of the file translated, slown down by a factor of one (AKA not slown down at all) with a pause of two seconds afterwards.</br>
	You can also also chain output strings using '/' (t,1,2/u,2,2).</br>
	The language option defines the language of the input file and sets the output language. Uses ISO 639-1 codes. ( http://www.loc.gov/standards/iso639-2/php/code_list.php )</br>
</br>
