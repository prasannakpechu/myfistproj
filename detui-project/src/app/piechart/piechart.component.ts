import { piechart } from '@angular/core';
 
@piechart({
  selector: 'piechart',
  templateUrl: './piechart.html'
})
export class PieChartComponent {
  // Pie
  public pieChartLabels:string[] = ['Not-in-family', 'Husband','Wife','Own-child','Unmarried','Other-relative'];
  public pieChartData:number[] = [8305, 13193, 1568 , 5068 ,3446 , 981];
  public pieChartType:string = 'pie';
 
  // events
  public chartClicked(e:any):void {
    console.log(e);
  }
 
  public chartHovered(e:any):void {
    console.log(e);
  }
}