using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DistanceBetweenTransforms : MonoBehaviour
{

    public Transform GameObject1Transform;
    public Transform GameObject2Transform;

    public float Distance;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        Distance = Vector3.Distance(GameObject1Transform.position, GameObject2Transform.position);
    }
}
