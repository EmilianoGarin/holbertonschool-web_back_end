import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const results = [];
  try {
    const valueToPresent = await signUpUser(firstName, lastName);
    results.push({ status: 'fulfilled', value: valueToPresent });
    await uploadPhoto(fileName);
  } catch (error) {
    results.push({ status: 'rejected', value: error.toString() });
  }
  return results;
}
