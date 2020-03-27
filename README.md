<p align="center">
  <a href="" rel="noopener">
 <img src="https://images.unsplash.com/photo-1538991452856-3bae8974c99c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&h=1000&q=80" alt="Project logo"></a>
</p>
<h3 align="center">Special Park</h3>

<div align="center">

[![Special Park](https://img.shields.io/badge/hackathon-name-orange.svg)](http://specialpark.nl)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/buzzzlightyear/special-park/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.md)

</div>

---

<p align="center"> A platform which provides a parking service with in depth statistics of user usage and automatic payment system.
    <br> 
</p>

## 📝 Table of Contents

- [Problem Statement](#problem_statement)
- [Idea / Solution](#idea)
- [Platform Components](#components)
- [Maintainers](#authors)
- [Product Owners](#po)

## 🧐 Problem Statement <a name = "problem_statement"></a>

When making use of a parking garage. We face two problems:

- Waste of papertickets;
- Waiting lines when driving in or out of the garages, and also at the payment terminal.

## 💡 Idea / Solution <a name = "idea"></a>

We want to build a platform on which users can register. With their account, they can go to different parking garages (associated with our platform). 

When they want to make use of the parking garage, they can easily drive inside the parking garage without rolling down the windows to get a paperticket. Our technical component installed by the garage, will scan your license plate and validate your account. Upon succes of validation, the gate will open. 

When you're done and want to leave, you can skip the payment terminal and drive straight to the exit. At the exit, the technical component will scan your license plate again. The system will process your expenses and then open the gate. 

The bill will be added to your total billing for that month. The total bill will be subtracted from your bank account at the end of every month.

## 📦 Platform Components <a name = "components"></a>

- [Consumer website](https://github.com/buzzzlightyear/special-park/tree/master/web), this is where the consumer can visit for information. The consumer can then also create an account. When the consumer has an account, they can view in depth statistics from their account.

- [Raspberry Pi 4](https://github.com/buzzzlightyear/special-park/tree/master/app), the technical component of the platfrom. Scans the license plate and communicates with the REST API for validation.

- [REST API](https://github.com/buzzzlightyear/special-park/tree/master/api), this component is in charge of processing all requests. This component is the only component which has access to the database.

## 🦸🏻‍♂ Maintainers <a name = "authors"></a>

<table>
  <tbody>
    <tr>
      <td align="center">
        <a href="https://github.com/buzzzlightyear">
          <img width="150" height="150" src="https://avatars2.githubusercontent.com/u/36703601?s=460&v=4">
          </br>
          Steven Soekha
        </a>
      </td>
      <td align="center">
        <a href="https://github.com/tim-vink">
          <img width="150" height="150" src="https://avatars0.githubusercontent.com/u/28394164?s=400&u=50a3e18a3ed3aad7753989329935c50977f54c95&v=4">
          </br>
          Tim Vink
        </a>
      </td>
      <td align="center">
        <a href="https://github.com/ILLUSIONack">
          <img width="150" height="150" src="https://scontent-amt2-1.xx.fbcdn.net/v/t1.0-1/31531602_1612879725447057_5402279220040695808_n.jpg?_nc_cat=104&_nc_sid=dbb9e7&_nc_ohc=gzw6rA4aPnsAX9mLe58&_nc_ht=scontent-amt2-1.xx&oh=8d174d394b98230831482f2058a51cbd&oe=5EA10F68">
          </br>
          Usman Siddiqui
        </a>
      </td>
      <td align="center">
        <a href="https://github.com/ahmadkurdo">
          <img width="150" height="150" src="https://scontent-ams4-1.xx.fbcdn.net/v/t1.0-9/15825752_837473716394296_3168531526687396920_n.jpg?_nc_cat=100&_nc_sid=7aed08&_nc_ohc=HqsxTERDt9cAX_nXPnC&_nc_ht=scontent-ams4-1.xx&oh=af09322ea6334ccebd3de911811a58f2&oe=5EA11FC9">
          </br>
          Ahmed Rasid
        </a>
      </td>
    </tr>
  <tbody>
</table>

See also the list of [contributors](https://github.com/buzzzlightyear/special-park/graphs/contributors) who participated in this project.

## 👥 Product Owners <a name = "po"></a>

- [CIMSOLUTIONS](https://www.cimsolutions.nl/) - Digital Agency
