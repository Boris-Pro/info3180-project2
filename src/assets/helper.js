export const name = "helper";

let callAPI = async (url_endpoint) => {
    const response = await fetch(url_endpoint);
    return response.json();
}

export let getCsrfToken = async () => {
    let csrf = await callAPI('/api/v1/csrf-token');
    return csrf
}

export let getUserId = async () => {
    let curr_ref = await callAPI('/api/v1/authenticated');
    return curr_ref
}

export let getJWTToken = async () => {
    let jwt_ref = await callAPI('/api/v1/jwt-token');
    return jwt_ref
}