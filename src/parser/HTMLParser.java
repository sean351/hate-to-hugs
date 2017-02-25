package parser;
import java.io.File;
import java.io.IOException;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

 
/**
* Java Program to parse/read HTML documents from File using Jsoup library.
* Jsoup is an open source library which allows Java developer to parse HTML
* files and extract elements, manipulate data, change style using DOM, CSS and
* JQuery like method.
*
* @author Javin Paul
*/
public class HTMLParser{
 
	 public static void main( String[] args )
	 {
	     String url = "http://en.wikipedia.org/wiki/Big_data";

	     Document document;
	     try {
	         document = Jsoup.connect(url).get();
	         Elements paragraphs = document.select("p");

	         Element firstParagraph = paragraphs.first();
	         Element lastParagraph = paragraphs.last();
	         Element p;
	         int i=1;
	         p=firstParagraph;
	         System.out.println("*  " +p.text());
	         while (p!=lastParagraph){
	             p=paragraphs.get(i);
	             System.out.println("*  " +p.text());
	             i++;
	         } 
	 } catch (IOException e) {
	     // TODO Auto-generated catch block
	     e.printStackTrace();
	 }}
}