import { Component } from '@angular/core';
import { ClientService } from './client.service'
import { first } from 'rxjs/operators';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  constructor(private service: ClientService){}

  functions = []
  input: string = ""
  ngOnInit(){}

  search(){
    this.service.send(this.input)
    .pipe(first()).subscribe(
      res => {
        console.log(res);
      },
      err => {
        console.log("Error occured : "+ err);
      }
    );
  }


}
