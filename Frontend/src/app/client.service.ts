import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ClientService {

  readonly ROOT_URL = environment.baseUrl;

  constructor(private http:HttpClient) { }

  public send(input:string){

    let body = {
      input: input,
    };

    return this.http.post<any>(this.ROOT_URL+'/functions/',body)
    .pipe(map(res => {
      return res;
    }));
  }
}
