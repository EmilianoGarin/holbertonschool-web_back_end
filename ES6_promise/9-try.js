export default function guardrail(mathFunction) {
  const queue = [];
  try {
    const successfulExec = mathFunction();
    queue.push(successfulExec);
  } catch (error) {
    queue.push(error.toString());
  } finally {
    queue.push('Guardrail was processed');
  }
  return queue;
}
