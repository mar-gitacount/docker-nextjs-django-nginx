'use client';
import React, { FC, useEffect, useState } from 'react'
import axios, { AxiosInstance } from 'axios'

type Todo = {
    id: string
    title: String
    body: String
}

export default function Hello() {
    const [todos, setTodo] = useState<Todo[]>([])
    // USA版ブヘラを実行する。
    const GetusaBucchererApi = async () => {
        console.log("ブヘラメソッド")
   
        try {
            const csrftoken = document.querySelector<HTMLInputElement>('[name=csrfmiddlewaretoken]')?.value;
            if (!csrftoken) throw new Error('CSRF token not found');
            const instance: AxiosInstance = axios.create({
                baseURL: 'http://localhost:8080',
                withCredentials: true,
                headers: {
                    'X-CSRFToken': csrftoken,
                },
            });
            const response = await instance.post('api/companytools/usaBucherer/')
            console.log(`アメリカ版のデータが返ってきてる？${response?.data}`)
        } catch (error) {
            console.log(error)
        }
    }

    const getAPIData = async () => {
        let instance: AxiosInstance
        console.log("ブヘラメソッド")
        instance = axios.create({
            baseURL: 'http://localhost:8080',
            withCredentials: true,
        })

        try {
            const response = await instance.get('api/todo/')
            console.log(response?.data)
            const tododata = response?.data as Todo[]
            setTodo(tododata)
        } catch (error) {
            console.log(error)
        }
    }
    return (
        <div>
            ボタンをおしてデータを抽出する。クッキーを有効にした
            <button onClick={() => GetusaBucchererApi()}>アメリカ版データを取得する</button>
            {/* <button onClick={() => getAPIData()}>click</button>
            {todos.map((item) => (
                <div key={item.id}>
                    <h1>{item.title}</h1>
                    <p>{item.body}</p>
                </div>
            ))} */}
           
        </div>

    )
}