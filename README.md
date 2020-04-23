#A CLI for translating and generating audio files


trscli <format> <input language>-<output language> <file>
#How to use it:
	trscli uses a three options.
	* A format
	* A language option
	* A file

	The format option specifies the output format of the audio file. It uses the following format: <translate (t) or don't translate (u)>,<slow factor>,<pause>.
	Format "t,1,2" will produce an audio file with each of the lines of the file translated, slown down by a factor of one (AKA not slown down at all) with a pause of two seconds afterwards.
	You can also also chain output strings using '/' (t,1,2/u,2,2).
	The language option defines the language of the input file and sets the output language. Uses ISO 639-1 codes. ( http://www.loc.gov/standards/iso639-2/php/code_list.php )

