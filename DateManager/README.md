<table class="tg">
  <tr>
    <th>Job</th>
    <th>Status</th>
    <th>create date</th>
    <th>modified date</th>
  </tr>
  <tr>
    <td>Seprate the Arithmatic operation and Date operation</td>
    <td><img src="http://progressed.io/bar/100" alt="" border=3 height=20 width=100></img></td>
    <td>29/01/2019</td>
    <td>30/01/2019</td>
  </tr>
  <tr>
    <td>Write code for Arithmatic operation</td>
    <td><img src="http://progressed.io/bar/100" alt="" border=3 height=20 width=100></img></td>
    <td>29/01/2019</td>
    <td>30/01/2019</td>
  </tr>
  <tr>
    <td>Write code for Date operation</td>
    <td><img src="http://progressed.io/bar/100" alt="" border=3 height=20 width=100></img></td>
    <td>31/01/2019</td>
    <td>05/02/2019</td>
  </tr>
  <tr>
    <td>Add try catch block for all over the code</td>
    <td><img src="http://progressed.io/bar/100" alt="" border=3 height=20 width=100></img></td>
    <td>01/02/2019</td>
    <td>05/02/2019</td>
  </tr>

  <tr>
    <td colspan=4><b>Tobe continnued...</b></td>

  </tr>
</table>


      <table  class="tg">
        <tr>
          <th>Date Manager<th>
          <th></th>
          <th></th>
        </tr>
        <tr>
          <td></td>
          <td>master</td>
          <td>DateHandler.py</td>
        </tr>
        <tr>
          <td></td>
          <td>sub</td>
          <td>DateAccepter.py</td>
          <td></td>
        </tr>
        <tr>
          <td></td>
          <td></td>
          <td>DayCalculator.py</td>
        </tr>
        <tr>
          <td></td>
          <td></td>
          <td>Today.py</td>
        </tr>
        <tr>
          <td></td>
          <td>divisional_Operator</td>
          <td>DateOperationSelection.py</td>
        </tr>
        <tr>
          <td></td>
          <td></td>
          <td>TasksDivision.py</td>
        </tr>
      </table>

#### 1. master
        contains DateHandler handles the various operation
        Select what operation you need to perform.
        and accordinly it will gives call to that particular function
        written in TasksDivision

#### 2. Sub
        DateAccepter to accept date
        DayCalculator to perform different operation dates
        Today to get information of today.

#### 1. divisional_Operator
        DateOperationSelection to choose perform operation on today's date or any alternate date_entry
        TasksDivision to decide what operation need to perform.

<i>If want to add new operation then add new function of that operation into the sub folder's DayCalculator and call its object in TasksDivision's of divisional_Operator and write its entry for Master's Datehandler as well</i>
