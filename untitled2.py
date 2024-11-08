{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "dc7ed0ac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Next in your CC course: Show you’re in the know about network security Hi Walid, Network security is a focus of paramount importance to employers seeking to protect their critical assets and data. Lean in and learn. In this Certified in Cybersecurity course chapter instruction, we’ll cover : Computer networking Network cyberthreats and attacks Network security infrastructure Advance your cybersecurity career goals as you work toward CC certification. Once certified, you’ll become an ISC2 member with full access to all the benefits it brings. F or technical issues associated with the course, please visit the Thank you, ISC2 Learn\n"
     ]
    }
   ],
   "source": [
    "from bs4 import BeautifulSoup\n",
    "import re\n",
    "\n",
    "html_content = '''\n",
    "<?xml version=\"1.0\" encoding=\"utf-8\"?><!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\"><html xmlns=\"http://www.w3.org/1999/xhtml\" lang=\"en\" xml:lang=\"en\"><head>\t<title>Next in your CC course: Show you’re in the know about network security</title>\t<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/></head><body><div>\n",
    "<p><span style=\"font-size: 14px;\"><span lang=\"EN-US\">Hi Walid,</span></span></p>\n",
    "</div>\n",
    "<div>\n",
    "<p><span style=\"font-size: 14px;\"><span lang=\"EN-GB\">Network security is a focus of paramount importance to employers seeking to protect their critical assets and data. Lean in and learn.</span></span></p>\n",
    "</div>\n",
    "<div>\n",
    "<div>\n",
    "<p><span style=\"font-size: 14px;\"><span lang=\"EN-GB\">In this Certified in Cybersecurity course chapter instruction, we’ll cover</span><span lang=\"EN-GB\">:</span></span></p>\n",
    "</div>\n",
    "<div>\n",
    "<ul style=\"list-style-type: disc;\">\n",
    "<li style=\"font-size: 14px;\">\n",
    "<p><span style=\"font-size: 14px;\"><span lang=\"EN-GB\">Computer networking</span></span></p>\n",
    "</li>\n",
    "<li style=\"font-size: 14px;\">\n",
    "<p><span style=\"font-size: 14px;\"><span lang=\"EN-GB\">Network cyberthreats and attacks</span></span></p>\n",
    "</li>\n",
    "<li style=\"font-size: 14px;\">\n",
    "<p><span style=\"font-size: 14px;\"><span lang=\"EN-GB\">Network security infrastructure</span></span></p>\n",
    "</li>\n",
    "</ul>\n",
    "</div>\n",
    "</div>\n",
    "<div>\n",
    "<p><span style=\"font-size: 14px;\"><span lang=\"EN-GB\"></span><span style=\"letter-spacing: 0.02rem;\"></span><a rel=\"noopener\" href=\"https://learn.isc2.org/d2l/common/dialogs/quickLink/quickLink.d2l?ou=9541&amp;type=content&amp;rcode=isc2-58425\" target=\"_self\" style=\"letter-spacing: 0.02rem;\">Access Chapter 4: Network Security</a></span></p>\n",
    "</div>\n",
    "<div>\n",
    "<p><span style=\"font-size: 14px;\"><span lang=\"EN-GB\">Advance your cybersecurity career goals as you work toward CC certification. Once certified, you’ll become an ISC2 member with full access to all the benefits it brings.</span></span></p>\n",
    "</div>\n",
    "<div>\n",
    "<p><span style=\"font-size: 14px;\"><span lang=\"EN-GB\"></span>F<span lang=\"EN-US\" style=\"letter-spacing: 0.02rem;\">or technical issues associated with the course, please visit the </span><a rel=\"noopener\" target=\"_blank\" href=\"https://community.brightspace.com/isc2/s/\" style=\"letter-spacing: 0.02rem;\"><span lang=\"EN-US\">ISC2 Learn Support Portal.</span></a></span></p>\n",
    "<p><span style=\"font-size: 14px;\"><span style=\"letter-spacing: 0.02rem;\">Thank you,<br></span><span style=\"letter-spacing: 0.02rem;\">ISC2 Learn</span></span></p>\n",
    "</div></body></html>\n",
    "'''\n",
    "\n",
    "# Parse the HTML content\n",
    "soup = BeautifulSoup(html_content, 'html.parser')\n",
    "\n",
    "# Remove all links\n",
    "for a in soup.find_all('a', href=True):\n",
    "    a.extract()\n",
    "\n",
    "# Extract text from the HTML\n",
    "text = soup.get_text(separator='\\n', strip=True)\n",
    "\n",
    "# Remove extra spaces and line breaks\n",
    "text = re.sub(r'\\s+', ' ', text)\n",
    "\n",
    "print(text)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "33a1c743",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Launch TryHackMe Business ( https://tryhackme.com/business ) ************ We're hiring =E2=9C=A8 ************ TryHackMe is continuing to experience rapid growth, and so we're looking fo= r talented individuals to join our team and help over two=C2=A0million=C2= =A0users learn cyber security! Full Time Remote Positions =C2=A0 Full Stack Engineer ( https://tryhackme.notion.site/Full-Stack-Engineer-Rea= ct-Rebuild-94349aee4d3f40a48a475457e1861451 ) to join our React rebuild squ= ad, and helping us scale TryHackMe to support millions of users. =C2=A0 Senior Software Engineer ( https://tryhackme.notion.site/Senior-Software-En= gineer-7131004a2698476580d7d37851f4e3df ) to lead a team of high performing= Software Engineers and develop high-quality software design and architectu= re. =C2=A0 Content Engineering Manager ( https://tryhackme.notion.site/tryhackme/Conte= nt-Engineering-Manager-4064c337fb814e5b90bf855a97ddcf9e ) to support our Co= ntent Engineers responsible for researching, writing, and engineering custo= m TryHackMe labs. =C2=A0 See other open roles ( https://tryhackme.notion.site/Careers-at-TryHackMe-6= bd665d7bd3448348d04fa06f4b4ef66 )=C2=A0=E2=86=92 TryHackMe Employment Benefits * Competitive Salary * 401k / Pension and Health Insurance * $2,000 Dedicated training budget * Flexi time & fully remote * Annual company retreat * Flexible career and learning development Newest Team Members * Marta, Growth Product Manager * Shelby, Content Engineering Manager * Isac, Full Stack Engineer * James, Full Stack Engineer * Steve, Full Stack Engineer * Stevan, Full Stack Engineer * James, Product Manager * Lou, Creative Design Manager Thank you for reading! The TryHackMe team. Facebook ( https://www.facebook.com/Try-Hack-Me-101040432182368 )Twitter ( = https://twitter.com/RealTryHackMe )Instagram ( https://www.instagram.com/re= altryhackme/ )LinkedIn ( https://www.linkedin.com/company/tryhackme/ ) Pinterest ( https://www.pinterest.co.uk/RealTryHackMe/ )TikTok ( https://ww= w.tiktok.com/@tryhackmeofficial ) Terms ( https://tryhackme.com/r/legal/terms-of-use ) | Unsubscribe ( http:/= /track.customer.io/unsubscribe/dgTK1QUDALqhkQG5oZEBAY1dCIaQfIoYkWgjp8BPzA= =3D=3D ) Copyright =C2=A9 TryHackMe. All rights reserved. --9bd212a4343ec68817493397a1db6d0da2506347d2678dd9e8286271e5e0 Content-Transfer-Encoding: quoted-printable Content-Type: text/html; charset=\"utf-8\"\n",
      "/n this is Launch TryHackMe Business ( https://tryhackme.com/business ) ************ We're hiring =E2=9C=A8 ************ TryHackMe is continuing to experience rapid growth, and so we're looking fo= r talented individuals to join our team and help over two=C2=A0million=C2= =A0users learn cyber security! Full Time Remote Positions =C2=A0 Full Stack Engineer ( https://tryhackme.notion.site/Full-Stack-Engineer-Rea= ct-Rebuild-94349aee4d3f40a48a475457e1861451 ) to join our React rebuild squ= ad, and helping us scale TryHackMe to support millions of users. =C2=A0 Senior Software Engineer ( https://tryhackme.notion.site/Senior-Software-En= gineer-7131004a2698476580d7d37851f4e3df ) to lead a team of high performing= Software Engineers and develop high-quality software design and architectu= re. =C2=A0 Content Engineering Manager ( https://tryhackme.notion.site/tryhackme/Conte= nt-Engineering-Manager-4064c337fb814e5b90bf855a97ddcf9e ) to support our Co= ntent Engineers responsible for researching, writing, and engineering custo= m TryHackMe labs. =C2=A0 See other open roles ( https://tryhackme.notion.site/Careers-at-TryHackMe-6= bd665d7bd3448348d04fa06f4b4ef66 )=C2=A0=E2=86=92 TryHackMe Employment Benefits * Competitive Salary * 401k / Pension and Health Insurance * $2,000 Dedicated training budget * Flexi time & fully remote * Annual company retreat * Flexible career and learning development Newest Team Members * Marta, Growth Product Manager * Shelby, Content Engineering Manager * Isac, Full Stack Engineer * James, Full Stack Engineer * Steve, Full Stack Engineer * Stevan, Full Stack Engineer * James, Product Manager * Lou, Creative Design Manager Thank you for reading! The TryHackMe team. Facebook ( https://www.facebook.com/Try-Hack-Me-101040432182368 )Twitter ( = https://twitter.com/RealTryHackMe )Instagram ( https://www.instagram.com/re= altryhackme/ )LinkedIn ( https://www.linkedin.com/company/tryhackme/ ) Pinterest ( https://www.pinterest.co.uk/RealTryHackMe/ )TikTok ( https://ww= w.tiktok.com/@tryhackmeofficial ) Terms ( https://tryhackme.com/r/legal/terms-of-use ) | Unsubscribe ( http:/= /track.customer.io/unsubscribe/dgTK1QUDALqhkQG5oZEBAY1dCIaQfIoYkWgjp8BPzA= =3D=3D ) Copyright =C2=A9 TryHackMe. All rights reserved. --9bd212a4343ec68817493397a1db6d0da2506347d2678dd9e8286271e5e0 Content-Transfer-Encoding: quoted-printable Content-Type: text/html; charset=\"utf-8\"\n"
     ]
    }
   ],
   "source": [
    "from bs4 import BeautifulSoup\n",
    "import re\n",
    "\n",
    "html_content = '''\n",
    "Launch TryHackMe Business ( https://tryhackme.com/business )\n",
    "\n",
    "************\n",
    "We're hiring\n",
    "=E2=9C=A8\n",
    "************\n",
    "\n",
    "TryHackMe is continuing to experience rapid growth, and so we're looking fo=\n",
    "r talented individuals to join our team and help over two=C2=A0million=C2=\n",
    "=A0users learn cyber security!\n",
    "\n",
    "Full Time Remote Positions\n",
    "\n",
    "=C2=A0\n",
    "\n",
    "Full Stack Engineer ( https://tryhackme.notion.site/Full-Stack-Engineer-Rea=\n",
    "ct-Rebuild-94349aee4d3f40a48a475457e1861451 ) to join our React rebuild squ=\n",
    "ad, and helping us scale TryHackMe to support millions of users.\n",
    "\n",
    "=C2=A0\n",
    "\n",
    "Senior Software Engineer ( https://tryhackme.notion.site/Senior-Software-En=\n",
    "gineer-7131004a2698476580d7d37851f4e3df ) to lead a team of high performing=\n",
    " Software Engineers and develop high-quality software design and architectu=\n",
    "re.\n",
    "\n",
    "=C2=A0\n",
    "\n",
    "Content Engineering Manager ( https://tryhackme.notion.site/tryhackme/Conte=\n",
    "nt-Engineering-Manager-4064c337fb814e5b90bf855a97ddcf9e ) to support our Co=\n",
    "ntent Engineers responsible for researching, writing, and engineering custo=\n",
    "m TryHackMe labs.\n",
    "\n",
    "=C2=A0\n",
    "\n",
    "See other open roles ( https://tryhackme.notion.site/Careers-at-TryHackMe-6=\n",
    "bd665d7bd3448348d04fa06f4b4ef66 )=C2=A0=E2=86=92\n",
    "\n",
    "TryHackMe Employment Benefits\n",
    "\n",
    "* Competitive Salary\n",
    "*\n",
    "401k / Pension and Health Insurance\n",
    "* $2,000 Dedicated training budget\n",
    "* Flexi time & fully remote\n",
    "* Annual company retreat\n",
    "* Flexible career and learning development\n",
    "Newest Team Members\n",
    "\n",
    "* Marta, Growth Product Manager\n",
    "* Shelby, Content Engineering Manager\n",
    "* Isac, Full Stack Engineer\n",
    "* James, Full Stack Engineer\n",
    "* Steve, Full Stack Engineer\n",
    "* Stevan, Full Stack Engineer\n",
    "* James, Product Manager\n",
    "* Lou, Creative Design Manager\n",
    "\n",
    "Thank you for reading!\n",
    "\n",
    "The TryHackMe team.\n",
    "\n",
    "Facebook ( https://www.facebook.com/Try-Hack-Me-101040432182368 )Twitter ( =\n",
    "https://twitter.com/RealTryHackMe )Instagram ( https://www.instagram.com/re=\n",
    "altryhackme/ )LinkedIn ( https://www.linkedin.com/company/tryhackme/ )\n",
    "Pinterest ( https://www.pinterest.co.uk/RealTryHackMe/ )TikTok ( https://ww=\n",
    "w.tiktok.com/@tryhackmeofficial )\n",
    "\n",
    "Terms ( https://tryhackme.com/r/legal/terms-of-use ) | Unsubscribe ( http:/=\n",
    "/track.customer.io/unsubscribe/dgTK1QUDALqhkQG5oZEBAY1dCIaQfIoYkWgjp8BPzA=\n",
    "=3D=3D )\n",
    "\n",
    "Copyright =C2=A9 TryHackMe. All rights reserved.\n",
    "--9bd212a4343ec68817493397a1db6d0da2506347d2678dd9e8286271e5e0\n",
    "Content-Transfer-Encoding: quoted-printable\n",
    "Content-Type: text/html; charset=\"utf-8\"\n",
    "'''\n",
    "\n",
    "# Parse the HTML content\n",
    "soup = BeautifulSoup(html_content, 'html.parser')\n",
    "\n",
    "# Extract text from the HTML\n",
    "text = soup.get_text(separator='\\n', strip=True)\n",
    "\n",
    "# Remove extra spaces and line breaks\n",
    "text = re.sub(r'\\s+', ' ', text)\n",
    "\n",
    "print(text)\n",
    "for a in soup.find_all('a', href=True):\n",
    "    a.extract()\n",
    "\n",
    "# Extract text from the HTML\n",
    "text = soup.get_text(separator='\\n', strip=True)\n",
    "\n",
    "# Remove extra spaces and line breaks\n",
    "text = re.sub(r'\\s+', ' ', text)\n",
    "print (\" this is \" + text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eaab2903",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
