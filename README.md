# Audio-book generator
This program will help you to generate an audio-book for each chapter of the book you want. Every chapter will be saved in a different file to make it easier to the reader to manipulate the audio (maybe the reader would want to upload it to any site like youtube to make it easier to people to hear it). 

In order to make work this audio-book generator, you have to install a module called `pyttsx3`. So run this command in your terminal.
```
pip install pyttsx3
```
Then, you have to take all of the text of the book you want to make and audio-book of and paste it in the book.txt file. The script is made in a way that you have so separate each chapter by your own. Its simple, just put a newline at the end of the title and then **put ``::`` at the end of the chapter so the program can separate each chapter**. 
```
Chaper 1
Foo.::Chapter 2
Bar
```
In this case, the program takes ``Chapter 1`` as if it was the title of the chapter, and ``Foo`` as the content of the chapter. Then, it will create an audio file with the name of the title it took and the content will be ``Foo``. The file``book.txt`` contains an example in spanish, but **you can take any other language**.

## License
```
Copyright © 2023 RODRIGO

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```