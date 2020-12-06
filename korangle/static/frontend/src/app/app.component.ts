import { Component, OnInit, AfterViewInit, ViewChild } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'vishal';
  req_data;
  res_data;
  displayedColumns = [ 'movie_title', 'movie_release_date', 'movie_upvotes'];
  @ViewChild(MatSort, {static:false}) sort: MatSort;


  constructor (private http: HttpClient){}
  ngOnInit(){
    this.http.get<any>('/api/get_data/').subscribe(data => {
      //this.req_data = data;
      this.req_data = new MatTableDataSource(<any> data);
      this.req_data.sort = this.sort;

      console.log(this.req_data);

    })
  }

  update(obj){
    console.log(obj);
    obj.movie_upvotes = obj.movie_upvotes + 1;
    this.http.post<any>('/api/post_data/', obj).subscribe(data => {
        this.res_data = data;
    })
    console.log(this.res_data);
  }
  down(elm){
  if (elm.movie_upvotes != 0){
  console.log(elm);
  elm.movie_upvotes = elm.movie_upvotes - 1;
  this.http.post<any>('/api/post_data/', elm).subscribe(data => {
        this.res_data = data;
    })
  }
  else{
    alert('invali');
  }

  }

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.req_data.filter = filterValue.trim().toLowerCase();
}


}
