<h3>DateManager</h3>

<table class="tg">
  <tr>
    <th colspan=4>Folder Structure</th>
  </tr>
  <tr>
    <td rowspan=6>DateManager</td>
    <td>master</td>
    <td>DateHandler.py</td>
  </tr>
  <tr>
    <td rowspan=3>sub</img></td>
    <td>DateAccepter.py</td>
  </tr>
  <tr>
    <td>DayCalculator.py</td>
  </tr>
  <tr>
    <td>Today.py</td>
  </tr>
  <tr>
    <td rowspan=2>divisional_Operator</td>
    <td>DateOperationSelection.py</td>
  </tr>
  <tr>
    <td>TasksDivision.py</td>
  </tr>
  <tr>
    <td colspan=4><b>Tobe continnued...</b></td>

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
